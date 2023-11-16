import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import clear_output
from tqdm.notebook import tqdm


sns.set_style("whitegrid")
plt.rcParams.update({"font.size": 15})


def plot_losses(train_losses, test_losses, train_accuracies, test_accuracies):
    clear_output()
    fig, axs = plt.subplots(1, 2, figsize=(13, 4))
    axs[0].plot(range(1, len(train_losses) + 1), train_losses, label="train")
    axs[0].plot(range(1, len(test_losses) + 1), test_losses, label="test")
    axs[0].set_ylabel("loss")

    axs[1].plot(range(1, len(train_accuracies) + 1), train_accuracies, label="train")
    axs[1].plot(range(1, len(test_accuracies) + 1), test_accuracies, label="test")
    axs[1].set_ylabel("accuracy")

    for ax in axs:
        ax.set_xlabel("epoch")
        ax.legend()

    plt.show()

