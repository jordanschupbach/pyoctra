
all:
  nix develop . --command bash -c "pip install .; python"
