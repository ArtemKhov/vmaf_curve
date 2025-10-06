from typing import List, Dict
from bitrate_analyzer import get_bitrate
from vmaf_calculator import calculate_vmaf
from json_parser import parse_vmaf_json, parse_vmaf_detailed  # Теперь импортируем из json_parser
from plot_generator import generate_plot
from report_result import print_results


def analyze_video_quality(resolutions: List[str], reference_video: str) -> None:
    """
    Основная функция для анализа качества видео для разных разрешений
    """

    bitrates: List[int] = []
    vmaf_scores: List[float] = []
    detailed_stats: List[Dict[str, float]] = []

    for res in resolutions:
        test_video = f'big_buck_bunny_{res}.mp4'
        json_file = f'vmaf_{res}.json'

        print(f"🔍 Обработка {res}...")

        try:
            # Получить битрейт
            bitrate = get_bitrate(test_video)
            bitrates.append(bitrate)

            # Рассчитать VMAF
            calculate_vmaf(reference_video, test_video, json_file)

            # Извлечь базовый VMAF
            vmaf = parse_vmaf_json(json_file)
            vmaf_scores.append(vmaf)

            # Извлечь детальную статистику (опционально)
            detailed_stat = parse_vmaf_detailed(json_file)
            detailed_stats.append(detailed_stat)

            print(f"✅ {res}: Битрейт = {bitrate} кбит/с, VMAF = {vmaf:.2f}")

        except Exception as e:
            print(f"❌ Ошибка при обработке {res}: {e}")
            continue

    # Генерация графика и вывод результатов
    if bitrates and vmaf_scores:
        generate_plot(bitrates, vmaf_scores, resolutions)
        print_results(resolutions, bitrates, vmaf_scores)

        print("\n📊 Детальная статистика VMAF:")
        for res, stats in zip(resolutions, detailed_stats):
            print(f"{res}: {stats}")
    else:
        print("⚠️  Нет данных для анализа")


def main() -> None:
    """
    Точка входа в программу анализа качества видео
    """
    resolutions = ['144p', '240p', '360p', '480p', '720p', '1080p']
    reference = 'big_buck_bunny_1080p24.y4m'

    print("🎬 Запуск анализа качества видео")
    analyze_video_quality(resolutions, reference)
    print("\n✅ Анализ завершен!")


if __name__ == "__main__":
    main()