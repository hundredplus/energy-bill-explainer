> Historical learning notes imported from the iMac. Current layout and setup are in README.md.

# Day 1 checklist

Your objective is to understand and verify the scaffold, not to add bill-calculation features.

## Block 1 Learn 60 minutes

- Review the Django project versus app distinction.
- Trace `manage.py` to `config.settings` and `config.urls`.
- Identify the purpose of `INSTALLED_APPS`, middleware, the database setting, WSGI and ASGI.
- Explain why secrets and environment-specific values should not be committed.

## Block 2 Build and run 3 hours

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and confirm the product caveat appears.

## Block 3 Prove 90 minutes

```bash
pytest
python manage.py check
ruff check .
```

The smoke test must prove that the root route responds and includes both the product name and the non-official-service caveat.

## Block 4 Explain 30 minutes maximum

Add no more than five bullets to `docs/interview_notes.md` answering:

- Why this project?
- Why is it a companion rather than an official comparison service?
- What is the difference between the Django project and the `bills` app?
- What happens between requesting `/` and receiving the response?
- Which configuration will change before production?

## Block 5 Career return 90 minutes

- Create an application tracker with role, employer, URL, fit, date, contact, status and follow-up date.
- Save the current CV as the baseline version.
- List eight target employers or live role families.
- Draft one truthful work-in-progress project bullet.

## End-of-day gate

Day 1 is complete only when:

- setup succeeds on your machine;
- the server starts and the landing response is visible;
- the smoke test, Django check and lint check pass;
- the README accurately describes scope and non-goals;
- the five interview bullets and application tracker exist;
- you make the initial Git commit yourself.
