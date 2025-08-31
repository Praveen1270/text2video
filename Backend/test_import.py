try:
    import api
    print("API imported successfully")
except Exception as e:
    print(f"Error importing API: {e}")
    import traceback
    traceback.print_exc()
