.PHONY: generate-reference-images run-tests

generate-reference-images:
	uv run python ./scripts/generate_reference_images.py

run-tests:
	uv run pytest tests/