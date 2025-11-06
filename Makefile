.PHONY: run
run:
	uv run fastapi dev app/main.py

.PHONY: test
test:
	uv run pytest