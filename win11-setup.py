import subprocess

programs = [
    "Python.Python.3.11",
    "Microsoft.VisualStudioCode",
    "Mozilla.Firefox",
    "Microsoft.PowerToys",
    "Google.Chrome",
    "Git.Git",
    "VideoLAN.VLC",
    "7zip.7zip"
]

for program_id in programs:
    print(f"Now attempting to install {len(programs)} programs vua winget.")
    try:
        print(f"\nInstalling {program_id}....")
        subprocess.run(
            ["winget", "install", "-e", "--id", program_id, "--accept-package-agreements", "--accept-source-agreements"],
            check=True
        )
        print(f"Installed {program_id} successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {program_id}.")