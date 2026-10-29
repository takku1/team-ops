"""Compact timeline of a Claude Code or Codex session for manual error analysis.

Prints user turns, assistant text (short), suite skill/file loads, tool calls, and tool errors.
"""
import json
import re
import sys

SUITE = re.compile(r'team-ops|team-lead|build-implementation-loop|build-code-review|build-definition-of-done|'
                   r'ai-context-management|ai-evaluation|plan-work-breakdown|plan-design-review|secure-review|'
                   r'design-product-workflow|check_runner|coordination\.md')


def short(text, n):
    return ' '.join(str(text).split())[:n]


def claude(lines):
    for e in lines:
        t, msg = e.get('type'), e.get('message', {})
        content = msg.get('content') if isinstance(msg, dict) else None
        if t == 'user':
            if isinstance(content, str):
                yield 'USER', short(content, 400)
            for b in content or []:
                if isinstance(b, dict) and b.get('type') == 'text':
                    yield 'USER', short(b['text'], 400)
                elif isinstance(b, dict) and b.get('type') == 'tool_result' and b.get('is_error'):
                    yield 'ERR', short(b.get('content'), 200)
        elif t == 'assistant':
            for b in content or []:
                if b.get('type') == 'text':
                    yield 'ASST', short(b['text'], 250)
                elif b.get('type') == 'tool_use':
                    inp = json.dumps(b.get('input', {}))
                    yield ('SUITE' if SUITE.search(inp) or b['name'] in ('Skill', 'Agent', 'Task') else 'TOOL'), f"{b['name']} {short(inp, 160)}"


def codex(lines):
    for e in lines:
        if e.get('type') != 'response_item':
            continue
        p = e['payload']
        k = p.get('type')
        if k == 'message' and p.get('role') in ('user', 'assistant'):
            text = ' '.join(c.get('text', '') for c in p.get('content', []))
            if p['role'] == 'user' and text.lstrip().startswith(('<', '#')):
                continue  # injected environment/instructions
            yield ('USER' if p['role'] == 'user' else 'ASST'), short(text, 400 if p['role'] == 'user' else 250)
        elif k in ('custom_tool_call', 'function_call'):
            inp = p.get('input') or p.get('arguments') or ''
            yield ('SUITE' if SUITE.search(inp) else 'TOOL'), f"{p.get('name')} {short(inp, 160)}"
        elif k in ('custom_tool_call_output', 'function_call_output'):
            out = p.get('output')
            text = ' '.join(c.get('text', '') for c in out) if isinstance(out, list) else str(out)
            if re.search(r'Script failed|error|Error|denied|not found|exit code [1-9]', text[:400]):
                yield 'ERR', short(text, 200)


def main():
    lines = [json.loads(l) for l in open(sys.argv[1], encoding='utf-8') if l.strip()]
    gen = codex(lines) if any(l.get('type') == 'session_meta' for l in lines[:3]) else claude(lines)
    keep = set(sys.argv[2].split(',')) if len(sys.argv) > 2 else {'USER', 'ASST', 'SUITE', 'ERR'}
    counts = {}
    for kind, text in gen:
        counts[kind] = counts.get(kind, 0) + 1
        if kind in keep:
            print(f'{kind:5} {text}')
    print('COUNTS', counts)


if __name__ == '__main__':
    main()
