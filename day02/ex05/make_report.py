from config import *
from analytics import Research


def main():
    research = Research(data)
    heads, tails = research.calculations.count
    prob1, prob2 = research.calculations.fraction
    predict = research.calculations.predict_random(num_of_steps)
    predict_tails = [i[0] for i in predict]
    predict_heads = [i[1] for i in predict]

    text = template.format(
        len(research.file_greader()),
        tails, heads,
        prob1, prob2,
        num_of_steps,
        sum(predict_tails), sum(predict_heads)
        )
    research.calculations.save_file(text, report)


if __name__ == '__main__':
    main()
