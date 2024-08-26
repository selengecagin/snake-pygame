import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores):
    """
    Plot the scores and mean scores of the game.

    This function creates a real-time plot of the game scores and mean scores
    over the course of training. It updates the plot after each game.

    Args:
        scores (list): List of scores from each game.
        mean_scores (list): List of mean scores up to each game.

    Returns:
        None

    Note:
        This function is designed to work in an IPython environment (like Jupyter notebooks)
        and uses interactive plotting.
    """
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)