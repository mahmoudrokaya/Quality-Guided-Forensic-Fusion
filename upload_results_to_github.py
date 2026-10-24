from pathlib import Path
import subprocess
import shutil
import sys
import tempfile
import os

# ============================================================
# Configuration
# ============================================================

SOURCE_RESULTS = Path(
    r"D:\47\472\New-Papers\Digital_Forensics_Framework_Network Intrusions\Experiments\Results"
)

REPO_URL = (
    "https://github.com/mahmoudrokaya/"
    "Reliability-Aware-Multi-View-Forensic-Evidence-Synthesis.git"
)

BRANCH = "main"

# Folder name to create inside the GitHub repository
DESTINATION_FOLDER = "Results"

COMMIT_MESSAGE = "Add experimental results"

# ============================================================
# Helper functions
# ============================================================

def run_git(args, cwd=None):
    """Run a Git command and stop if it fails."""
    cmd = ["git"] + args

    print("\n>", " ".join(cmd))

    result = subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    print(result.stdout)

    if result.returncode != 0:
        raise RuntimeError(
            f"Git command failed with exit code {result.returncode}"
        )

    return result.stdout


def check_git_installed():
    try:
        run_git(["--version"])
    except Exception:
        print(
            "\nERROR: Git is not installed or is not available in PATH."
        )
        print(
            "Install Git for Windows first, then run this script again."
        )
        sys.exit(1)


def copy_directory_contents(source, destination):
    """
    Copy the complete source directory recursively to destination.
    Existing files with the same names are replaced.
    """
    destination.mkdir(parents=True, exist_ok=True)

    for item in source.iterdir():

        target = destination / item.name

        if item.is_dir():

            if target.exists():
                shutil.rmtree(target)

            shutil.copytree(item, target)

        else:

            shutil.copy2(item, target)


# ============================================================
# Main
# ============================================================

def main():

    print("=" * 72)
    print("GitHub Results Uploader")
    print("=" * 72)

    # --------------------------------------------------------
    # Validate local source
    # --------------------------------------------------------

    if not SOURCE_RESULTS.exists():
        print("\nERROR: Source directory does not exist:")
        print(SOURCE_RESULTS)
        sys.exit(1)

    if not SOURCE_RESULTS.is_dir():
        print("\nERROR: Source path is not a directory:")
        print(SOURCE_RESULTS)
        sys.exit(1)

    check_git_installed()

    # --------------------------------------------------------
    # Temporary clone directory
    # --------------------------------------------------------

    temp_root = Path(tempfile.mkdtemp(prefix="github_results_upload_"))

    repo_dir = temp_root / "repository"

    print("\nTemporary working directory:")
    print(temp_root)

    try:

        # ----------------------------------------------------
        # Clone main branch
        # ----------------------------------------------------

        print("\nCloning repository...")

        run_git(
            [
                "clone",
                "--branch",
                BRANCH,
                "--single-branch",
                REPO_URL,
                str(repo_dir),
            ]
        )

        # ----------------------------------------------------
        # Ensure correct branch
        # ----------------------------------------------------

        run_git(["checkout", BRANCH], cwd=repo_dir)

        run_git(["pull", "--ff-only", "origin", BRANCH], cwd=repo_dir)

        # ----------------------------------------------------
        # Destination inside repository
        # ----------------------------------------------------

        destination = repo_dir / DESTINATION_FOLDER

        print("\nLocal source:")
        print(SOURCE_RESULTS)

        print("\nRepository destination:")
        print(destination)

        # ----------------------------------------------------
        # Copy files recursively
        # ----------------------------------------------------

        print("\nCopying Results directory...")

        copy_directory_contents(
            SOURCE_RESULTS,
            destination,
        )

        print("\nCopy completed.")

        # ----------------------------------------------------
        # Git status
        # ----------------------------------------------------

        run_git(["status", "--short"], cwd=repo_dir)

        # ----------------------------------------------------
        # Add all changes under Results
        # ----------------------------------------------------

        run_git(
            ["add", "--all", DESTINATION_FOLDER],
            cwd=repo_dir,
        )

        # ----------------------------------------------------
        # Check whether anything actually changed
        # ----------------------------------------------------

        diff_result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=repo_dir,
        )

        if diff_result.returncode == 0:

            print("\nNo changes detected.")
            print("The GitHub Results folder already matches the local folder.")
            return

        # ----------------------------------------------------
        # Commit
        # ----------------------------------------------------

        run_git(
            ["commit", "-m", COMMIT_MESSAGE],
            cwd=repo_dir,
        )

        # ----------------------------------------------------
        # Push
        # ----------------------------------------------------

        print("\nPushing to GitHub...")

        run_git(
            ["push", "origin", BRANCH],
            cwd=repo_dir,
        )

        print("\n" + "=" * 72)
        print("UPLOAD COMPLETED SUCCESSFULLY")
        print("=" * 72)

        print(
            "\nRepository:"
            "\nhttps://github.com/mahmoudrokaya/"
            "Reliability-Aware-Multi-View-Forensic-Evidence-Synthesis"
        )

        print(
            "\nUploaded to:"
            f"\n{BRANCH}/{DESTINATION_FOLDER}"
        )

    except Exception as exc:

        print("\n" + "=" * 72)
        print("UPLOAD FAILED")
        print("=" * 72)

        print(f"\n{exc}")

        print(
            "\nIf Git asks for authentication, allow Git Credential Manager "
            "to use your saved GitHub account."
        )

        sys.exit(1)

    finally:

        # Remove the temporary repository clone
        if temp_root.exists():
            print("\nRemoving temporary working directory...")
            shutil.rmtree(temp_root, ignore_errors=True)


if __name__ == "__main__":
    main()