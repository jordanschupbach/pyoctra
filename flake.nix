
{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    flake-utils,
    nixpkgs,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        devShells.aiestate = pkgs.mkShell {

          buildInputs = [ 

            pkgs.gcc
            pkgs.git
            pkgs.gnumake
            pkgs.just
            pkgs.just 
            pkgs.lapack
            pkgs.libxml2 
            pkgs.poetry
            pkgs.python313
            pkgs.python313Packages.pip

          ];

          shellHook = ''
            python -m venv .venv
            source .venv/bin/activate
            pip install .
          '';

        };

        devShell = self.devShells.${system}.aiestate;

      }
    );
}




# pkgs.mkShell {
#             # The Nix packages provided in the environment
#             packages = [
#               pkgs.python311
#               pkgs.python311Packages.pip
#               # Whatever other packages are required
#             ];
#             shellHook = ''
#               python -m venv .venv
#               source .venv/bin/activate
#               pip install -r requirements.txt
#             '';
#
