from typing import List


def print_results(resolutions: List[str], bitrates: List[int], vmaf_scores: List[float]) -> None:
    """
    Вывод таблицы результатов анализа
    """

    if len(resolutions) != len(bitrates) or len(resolutions) != len(vmaf_scores):
        raise ValueError("Все списки должны иметь одинаковую длину")

    print("\nРезультаты анализа качества видео:")
    print("=" * 45)
    print(f"{'Разрешение':<10} | {'Битрейт (кбит/с)':<16} | {'VMAF':<6}")
    print("-" * 45)

    for res, bitrate, vmaf in zip(resolutions, bitrates, vmaf_scores):
        print(f"{res:<10} | {bitrate:<16} | {vmaf:<6.2f}")

    print("-" * 45)

    avg_vmaf = sum(vmaf_scores) / len(vmaf_scores)
    max_vmaf = max(vmaf_scores)
    min_vmaf = min(vmaf_scores)

    print(f"\nСтатистика:")
    print(f"Средний VMAF: {avg_vmaf:.2f}")
    print(f"Максимальный VMAF: {max_vmaf:.2f}")
    print(f"Минимальный VMAF: {min_vmaf:.2f}")