"""
This file contains functions for file system management, to be used as tools by Gemini.
"""
import os
import shutil


def list_files(directory: str) -> dict:
    """List files and folders in the directory.

    Args:
        directory: Directory to list files and folders for.

    Returns:
        A dictionary describing whether the operation was successful, and either the list of files or an error message.
    """
    try:
        items = os.listdir(directory)
        return {"success": True, "items": items}
    except Exception as e:
        return {"success": False, "error": str(e)}

def move_file(src: str, dst: str) -> dict:
    """Moves a file or a directory from a source path to a destination folder.
    Raises an error if the destination exists.

    Args:
        src: Path of the file to move.
        dst: Destination path where to move the file.

    Returns:
        A dictionary describing whether the operation was successful, and an optional error message.
    """
    try:
        if os.path.exists(dst):
            raise FileExistsError(f"Destination '{dst}' already exists.")
        shutil.move(src, dst)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

def copy_file(src: str, dst: str) -> dict:
    """Copies a file or a directory at a source path into a destination folder.
    Raises an error if the destination exists.

    Args:
        src: Path of the file to copy.
        dst: Destination path where to copy the file.

    Returns:
        A dictionary describing whether the operation was successful, and an optional error message.
    """
    try:
        if os.path.exists(dst):
            raise FileExistsError(f"Destination '{dst}' already exists.")
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

def delete_file(path: str) -> dict:
    """Deletes a file or directory.

    Args:
        path: Path of the file to delete.

    Returns:
        A dictionary describing whether the operation was successful, and an optional error message.
    """
    try:
        os.remove(path)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}


def create_file(path: str, content: str = "") -> dict:
    """Creates a new file with optional content.

    Args:
        path: Path of the file to create.
        content: String content to write into the file

    Returns:
        A dictionary describing whether the operation was successful, and an optional error message.
    """
    try:
        with open(path, "w") as f:
            f.write(content)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}


file_system_management_tools = [
    list_files,
    move_file,
    copy_file,
    create_file
]