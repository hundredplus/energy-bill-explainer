> Historical learning notes imported from the iMac. Current layout and setup are in README.md.

# Interview notes

Keep each daily entry to 30 minutes and four or five bullets.

## Day 1 project choice and request flow

- **What I built:** A clean Django project, a domain app, environment-aware settings, a root route and a smoke test.
- **Why this project:** It solves a recognisable Australian household problem while demonstrating backend, API, database, testing and integration skills.
- **Product boundary:** It explains and prepares information; official tools remain the authority for comparison and switching decisions.
- **Request flow:** The root URL pattern resolves to a view, which returns an HTTP response. Later flows will add serializer, service and database layers only where needed.
- **Production risk:** Development defaults must never be mistaken for production configuration; secrets, hosts, database and deployment checks will be hardened later.

## Daily template

- Topic:
- What I built:
- Why it matters:
- Production risk or trade-off:
- Code and tests that prove it:
