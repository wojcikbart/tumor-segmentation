import os
import synapseclient

# Authenticate using your personal access token
syn = synapseclient.Synapse()
syn.login(authToken="eyJ0eXAiOiJKV1QiLCJraWQiOiJXN05OOldMSlQ6SjVSSzpMN1RMOlQ3TDc6M1ZYNjpKRU9VOjY0NFI6VTNJWDo1S1oyOjdaQ0s6RlBUSCIsImFsZyI6IlJTMjU2In0.eyJhY2Nlc3MiOnsic2NvcGUiOlsidmlldyIsImRvd25sb2FkIiwibW9kaWZ5Il0sIm9pZGNfY2xhaW1zIjp7fX0sInRva2VuX3R5cGUiOiJQRVJTT05BTF9BQ0NFU1NfVE9LRU4iLCJpc3MiOiJodHRwczovL3JlcG8tcHJvZC5wcm9kLnNhZ2ViYXNlLm9yZy9hdXRoL3YxIiwiYXVkIjoiMCIsIm5iZiI6MTc0OTA2NTU5MywiaWF0IjoxNzQ5MDY1NTkzLCJqdGkiOiIyMTI3NSIsInN1YiI6IjM1NDU2ODEifQ.cQ3CpazVBt4FZcYVkmb3tw8GJBQkYTr28AR7dJBcYPCc3fRT-7IeZrg2_mNTnB0SaTIwahYhQ_ylxfUnnKslBMxYPuPLjyDCvHSD_wXYIPC9CiG1mpCh7FJw0dXX7wop3gJN-mzmkTOd4RF3-TopENu0ZjY3qoOq6_00CkUwCbVpFeZCgZ6nh9iN_RLk22h_b4GvkRAZSml4L0F4k5TZDreb6DZ4sZfb-A23-G3_fB4qVjb5lkepYdvdNLzYJtFi6IsMRUbxVQWiQsXw8F2eZVtsFt7Adw27gu75Jz8TP8BcUipNzlsCyaZ6Xo4osYJ6P_mxYYGTMpzZ7mxCnrranQ")  # ← paste your token

download_dir = r"brats_data"
os.makedirs(download_dir, exist_ok=True)

# Download a file by Synapse ID, specifying the download location
entity_id = "syn60086071"  # ID of the file (not a folder)
# Available ids
# "syn64908826" - BraTS2024Pre
# "syn60086071" - BraTS2024Post
# "syn51692615" - BraTS2024Africa

file_entity = syn.get(entity_id, downloadLocation=download_dir)



# Local file path after download
local_path = file_entity.path
print(f"Downloaded to: {local_path}")