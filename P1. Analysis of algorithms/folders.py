import os

def create_folder_structure(folder_path):
  """
  Creates a folder structure based on the provided list of folders.

  Args:
    folder_path: The base path where the folder structure will be created.
  """

  folders = [
    "P1. Analysis of algorithms",
    "P2. Basic Mathematics",
    "P3. Bit Manipulation",
    "P4. Recursion",
    "P5. Arrays",
    "P6. 2D Arrays",
    "P7. Searching Algorithms",
    "P8. Sorting Algorithms",
    "P9. Matrix",
    "P10. Hashing",
    "P11. Strings",
    "P12. LinkedList",
    "P13. Stacks"
  ]

  for folder in folders:
    folder_path_full = os.path.join(folder_path, folder)
    os.makedirs(folder_path_full, exist_ok=True)

if __name__ == "__main__":
  base_path = "D:\PDSA"
  create_folder_structure(base_path)