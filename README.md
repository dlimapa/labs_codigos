# labs_codigos
Repositório para teste de códigos diversos

Para o erro

```text
Pushing to https://github.com/dlimapa/labs_codigos.git
Missing or invalid credentials.
Error: socket hang up
    at connResetException (internal/errors.js:610:14)
    at Socket.socketOnEnd (_http_client.js:453:23)
    at Socket.emit (events.js:327:22)
    at endReadableNT (_stream_readable.js:1220:12)
    at processTicksAndRejections (internal/process/task_queues.js:84:21) {
  code: 'ECONNRESET'
```
```shell
git remote set-url origin https://github.com/dlimapa/labs_codigos.git

git remote set-url origin https://dlimapa:password_github@github.com/dlimapa/labs_codigos.git

```