.PHONY: validate validate-repo

validate: validate-repo

validate-repo:
	python3 scripts/validate-repo.py
