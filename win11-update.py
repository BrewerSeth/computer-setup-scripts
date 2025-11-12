# Import the subprocess module to run command-line programs from Python
import subprocess

# Print a message indicating we're starting the update process
print("Now attempting to update all winget programs...")

# Run the winget upgrade command for all programs
# --all updates every installed program
# -h = silent installation (no user prompts)
# --accept-package-agreements automatically accepts license agreements
# --accept-source-agreements automatically accepts source agreements
# --disable-interactivity = disable all interactive prompts
result = subprocess.run(
    ["winget", "upgrade", "--all", "-h", "--accept-package-agreements", "--accept-source-agreements", "--disable-interactivity"],
    capture_output=True,
    text=True
)

# Print that the update process is complete
print("\nUpdate process completed.")

# Print the output from winget so you can see what happened
print("\nWinget output:")
print(result.stdout)

# Now update Windows itself
print("\n" + "="*50)
print("Now checking for Windows Updates...")
print("="*50)

# Ask user if they want to auto-reboot after Windows updates
print("\nWindows updates may require a reboot.")
reboot_choice = input("Do you want to automatically reboot if needed? (y/n): ").strip().lower()

# Build the PowerShell command based on user choice
if reboot_choice == 'y':
    ps_command = "Install-Module -Name PSWindowsUpdate -Force -SkipPublisherCheck; Import-Module PSWindowsUpdate; Get-WindowsUpdate -AcceptAll -Install -AutoReboot"
    print("\nInstalling Windows updates with auto-reboot enabled (this may take a while)...")
else:
    ps_command = "Install-Module -Name PSWindowsUpdate -Force -SkipPublisherCheck; Import-Module PSWindowsUpdate; Get-WindowsUpdate -AcceptAll -Install"
    print("\nInstalling Windows updates without auto-reboot (this may take a while)...")

# Use PowerShell to install Windows updates via PSWindowsUpdate module
# This requires the PSWindowsUpdate module to be installed
windows_update_result = subprocess.run(
    ["powershell", "-Command", ps_command],
    capture_output=True,
    text=True
)

# Print Windows update results
print("\nWindows Update output:")
print(windows_update_result.stdout)
if windows_update_result.stderr:
    print("Errors/Warnings:")
    print(windows_update_result.stderr)

print("\n" + "="*50)
print("All updates completed!")
print("="*50)
