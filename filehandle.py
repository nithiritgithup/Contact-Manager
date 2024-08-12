import os
if os.path.exists("nith"):
    os.rmdir("nith")
    print("dir deleted successfully")
else:
    print("dir not found")