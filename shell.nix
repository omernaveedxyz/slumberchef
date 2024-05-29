{pkgs}: {
  default = pkgs.mkShell {
    # List of packages to add to the shell environment
    packages = with pkgs; [
      nodejs
      (pkgs.python3.withPackages (python-pkgs: [
        python-pkgs.requests
        python-pkgs.beautifulsoup4
      ]))
    ];
  };
}
