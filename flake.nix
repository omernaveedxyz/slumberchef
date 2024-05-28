{
  inputs = {
    # Externally extensible flake systems
    systems.url = "github:nix-systems/x86_64-linux";

    # Nix Packages collection & NixOS
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    # Pure Nix flake utility functions
    flake-utils.url = "github:numtide/flake-utils";
    flake-utils.inputs.systems.follows = "systems";
  };

  outputs = {
    nixpkgs,
    flake-utils,
    ...
  }: let
    inherit (nixpkgs.lib) genAttrs;
    inherit (flake-utils.lib) defaultSystems;

    # Create attribute set of default systems from flake-utils
    genAttrsFromDefaultSystems = genAttrs defaultSystems;

    # Extended Nixpkgs collection with additional and modified packages
    legacyPackages = genAttrsFromDefaultSystems (system:
      import nixpkgs {
        inherit system;
      });
  in {
    # Run a bash shell that provides the development environment
    # Usage: `nix develop`
    devShells = genAttrsFromDefaultSystems (system: import ./shell.nix {pkgs = legacyPackages.${system};});

    # Reformat code in the standard style
    # Usage: `nix fmt`
    formatter = genAttrsFromDefaultSystems (system: legacyPackages.${system}.alejandra);
  };
}
