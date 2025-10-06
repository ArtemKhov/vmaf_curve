import subprocess
from typing import Optional


def get_bitrate(video_file: str) -> Optional[int]:
    """
    Получить битрейт видео файла в кбит/с.
    """

    try:
        cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
               '-show_entries', 'stream=bit_rate', '-of', 'csv=p=0', video_file]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        bitrate_str = result.stdout.strip()
        if not bitrate_str:
            raise ValueError(f"Не удалось извлечь битрейт из файла: {video_file}")

        return int(bitrate_str) // 1000

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ошибка выполнения ffprobe для файла {video_file}: {e}")
    except ValueError as e:
        raise ValueError(f"Некорректный формат битрейта для файла {video_file}: {e}")