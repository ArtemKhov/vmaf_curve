import json
from typing import Dict, Any


def parse_vmaf_json(json_file: str) -> float:
    """
    Извлечение среднего VMAF из JSON файла.
    """

    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data: Dict[str, Any] = json.load(f)

        # Извлекаем среднее значение VMAF из структуры JSON
        vmaf_mean = data['pooled_metrics']['vmaf']['mean']
        return float(vmaf_mean)

    except KeyError as e:
        raise KeyError(f"Отсутствует ожидаемое поле в JSON файле {json_file}: {e}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Некорректный JSON формат в файле {json_file}: {e}")


def parse_vmaf_detailed(json_file: str) -> Dict[str, Any]:
    """
    Извлечение детальной статистики VMAF из JSON файла.
    """

    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data: Dict[str, Any] = json.load(f)

        vmaf_metrics = data['pooled_metrics']['vmaf']
        return {
            'mean': float(vmaf_metrics['mean']),
            'min': float(vmaf_metrics['min']),
            'max': float(vmaf_metrics['max']),
        }

    except KeyError as e:
        raise KeyError(f"Отсутствует ожидаемое поле в JSON файле {json_file}: {e}")