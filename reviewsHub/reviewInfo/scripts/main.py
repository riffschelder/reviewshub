from summarize import SimpleSummarizer
Simple = SimpleSummarizer()
input = "This is, without question, the best phone I have ever owned. It is fast, smooth, and fluid.I was a long time HTC user, and was a little concerned about going to Samsung. Well, it was no problem whatsoever. There was basically zero learning curve. The features are cool and useful, but quite intuitive. The facial recognition unlock is simply awesome! That, combined with the excellent voice command options and voice typing make this an extremely capable one-handed device for me. The 4G hotspot works beautifully, and doesn't destroy my battery life. Ah yes, the battery. Excellent for such a beast of a phone! It's a smartphone. It's not going to last 3 days. But, with moderate use, including calls, data, camera, hotspot, etc., it easily makes it through the day."
print Simple.summarize(input,3)
