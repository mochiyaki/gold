# nix/packages.nix — Gold Agent package built with uv2nix
{ inputs, ... }: {
  perSystem = { pkgs, system, ... }:
    let
      goldVenv = pkgs.callPackage ./python.nix {
        inherit (inputs) uv2nix pyproject-nix pyproject-build-systems;
      };

      # Import bundled skills, excluding runtime caches
      bundledSkills = pkgs.lib.cleanSourceWith {
        src = ../skills;
        filter = path: _type:
          !(pkgs.lib.hasInfix "/index-cache/" path);
      };

      runtimeDeps = with pkgs; [
        nodejs_20 ripgrep git openssh ffmpeg tirith
      ];

      runtimePath = pkgs.lib.makeBinPath runtimeDeps;
    in {
      packages.default = pkgs.stdenv.mkDerivation {
        pname = "gold";
        version = (builtins.fromTOML (builtins.readFile ../pyproject.toml)).project.version;

        dontUnpack = true;
        dontBuild = true;
        nativeBuildInputs = [ pkgs.makeWrapper ];

        installPhase = ''
          runHook preInstall

          mkdir -p $out/share/gold $out/bin
          cp -r ${bundledSkills} $out/share/gold/skills

          ${pkgs.lib.concatMapStringsSep "\n" (name: ''
            makeWrapper ${goldVenv}/bin/${name} $out/bin/${name} \
              --suffix PATH : "${runtimePath}" \
              --set GOLD_BUNDLED_SKILLS $out/share/gold/skills
          '') [ "gold" "gold" "gold-acp" ]}

          runHook postInstall
        '';

        meta = with pkgs.lib; {
          description = "AI agent with advanced tool-calling capabilities";
          homepage = "https://github.com/mochiyaki/gold";
          mainProgram = "gold";
          license = licenses.mit;
          platforms = platforms.unix;
        };
      };
    };
}
