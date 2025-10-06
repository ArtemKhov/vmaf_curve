import matplotlib.pyplot as plt
from typing import List


def generate_plot(bitrates: List[int], vmaf_scores: List[float],
                  resolutions: List[str], output_file: str = 'vmaf_vs_bitrate.png') -> None:
    """
    Генерация графика зависимости VMAF от битрейта.
    """
    
    if len(bitrates) != len(vmaf_scores) or len(bitrates) != len(resolutions):
        raise ValueError("Все списки должны иметь одинаковую длину")

    plt.figure(figsize=(12, 8))
    plt.plot(bitrates, vmaf_scores, 'o-', linewidth=2, markersize=8)
    plt.xlabel('Битрейт (кбит/с)', fontsize=12)
    plt.ylabel('VMAF Score', fontsize=12)
    plt.title('Зависимость качества видео (VMAF) от битрейта', fontsize=14)
    plt.grid(True, alpha=0.3)

    # Аннотации для каждой точки
    for i, (bitrate, vmaf, res) in enumerate(zip(bitrates, vmaf_scores, resolutions)):
        plt.annotate(
            f'{res}\n({vmaf:.1f})',
            (bitrate, vmaf),
            xytext=(10, 10),
            textcoords='offset points',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
            fontsize=9
        )

    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.show()

    print(f"График сохранен как: {output_file}")