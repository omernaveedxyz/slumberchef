{pkgs}: {
  default = pkgs.mkShell {
    # List of packages to add to the shell environment
    packages = with pkgs; [
      nodejs
    ];
  };
}
