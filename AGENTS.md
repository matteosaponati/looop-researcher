## Rules
- Keep dependecies minimal and justified.
- Never commits datasets, model artifacts, or run outputs.
- Apply changes without backward compatibility unless I directly specify for it.
- After every major change, check again if you respected all the rules stated in the AGENTS.md.
- After every major change, update a log of the change in docs/logs/.
## Never Run
- Destructive cleanup: `rm -rf` outside clearly scoped temp paths.
- History rewrites without explicit request: `git reset --hard`, `git rebase -i`.
- Force pushes: `git push --force`.
- Any command that writes secrets to the repo.
