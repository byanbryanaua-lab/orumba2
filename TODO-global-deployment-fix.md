# TODO: Global deployment fix

- [x] Inspect `api/index.py` to confirm it is (or is not) a proxy/handler for Flask.
- [ ] Fix `render.yaml` indentation + ensure `startCommand` points to the correct WSGI export.
- [x] Fix `vercel.json` routing/build to serve Flask app via `wsgi.py` (not `api/index.py`).
- [x] Ensure static assets `/static/...` resolve globally.
- [x] Fix mobile navbar dropdown reliability by adjusting `_header.html` click logic (prevent premature drawer close on dropdown interactions).
- [ ] Deploy and verify:
  - [ ] `GET /` returns HTML
  - [ ] `GET /api/public/posts` returns JSON
  - [ ] `GET /static/css/...` returns 200
  - [ ] Mobile hamburger opens drawer
  - [ ] Mobile dropdown taps expand/collapse correctly (no instant close)

