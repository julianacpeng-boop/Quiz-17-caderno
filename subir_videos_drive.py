import json
import os
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

PASTA = Path("output_juh_caderno")
SCOPES = ["https://www.googleapis.com/auth/drive.file"]


def main():
    raw = os.environ.get("GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON", "").strip()
    folder_id = os.environ.get("GOOGLE_DRIVE_FOLDER_ID", "").strip()
    if not raw or not folder_id:
        raise RuntimeError(
            "Configure GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON (secret) e "
            "GOOGLE_DRIVE_FOLDER_ID (variable) no repositório."
        )

    info = json.loads(raw)
    credentials = service_account.Credentials.from_service_account_info(
        info, scopes=SCOPES
    )
    drive = build("drive", "v3", credentials=credentials, cache_discovery=False)

    videos = sorted(PASTA.glob("*.mp4"))
    if not videos:
        raise FileNotFoundError(f"Nenhum vídeo encontrado em {PASTA}")

    for video in videos:
        metadata = {"name": video.name, "parents": [folder_id]}
        media = MediaFileUpload(str(video), mimetype="video/mp4", resumable=True)
        uploaded = drive.files().create(
            body=metadata, media_body=media, fields="id,name"
        ).execute()
        print(f"Enviado ao Drive: {uploaded['name']} ({uploaded['id']})")


if __name__ == "__main__":
    main()
