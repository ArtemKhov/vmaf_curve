import subprocess
import json
from typing import Dict, Any


def calculate_vmaf(reference_video: str, test_video: str, output_json: str) -> None:
    """
    Расчет VMAF между референсным и тестовым видео.
    """

    try:
        if test_video != 'big_buck_bunny_1080p.mp4':
            cmd = [
                'ffmpeg', '-i', reference_video, '-i', test_video,
                '-lavfi',
                f"[1:v]scale=1920:1080:flags=lanczos[scaled];[0:v][scaled]libvmaf=log_path={output_json}:log_fmt=json",
                '-f', 'null', '-'
            ]
        else:
            cmd = [
                'ffmpeg', '-i', reference_video, '-i', test_video,
                '-lavfi', f"libvmaf=log_path={output_json}:log_fmt=json",
                '-f', 'null', '-'
            ]

        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ошибка выполнения ffmpeg VMAF расчета: {e}\nStderr: {e.stderr}")