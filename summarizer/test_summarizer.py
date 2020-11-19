from summarizer.summarizer import summarize


def test_summarize_whenPassedEmptyString_ReturnsEmpty():
    assert summarize("") == ""