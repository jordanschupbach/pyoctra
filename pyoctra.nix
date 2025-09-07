{
  lib,
  # pkg deps
  stdenv,
  python,
  fetchPypi,
  # python deps
  setuptools,
  buildPythonPackage,
}: let
in
  buildPythonPackage rec {
    pname = "pyoctra";
    version = "0.0.1";
    # pyproject = true;
    format = "pyproject";
    # format = "setup";

    src = ./.; # Current directory

    build-system = [setuptools];

    # Fetch from a local source or a specific archive if needed
    # src = fetchPypi { ... };

    # TODO: check if necessary
    preCheck = ''
      pushd $out
      export PATH=$PATH:$out/bin
    '';

    # TODO: check if necessary
    postCheck = ''
      popd
    '';

    meta = {
      description = "Python bindings to the OCTRA package";
      homepage = "";
      license = lib.licenses.unlicense;
      maintainers = with lib.maintainers; [];
    };
  }
