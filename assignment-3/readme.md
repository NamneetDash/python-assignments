1 — Basics of Probability

(a) Coin tosses (10,000 tosses)
What I did: simulated 10,000 fair coin tosses with a loop and counted heads vs tails, then computed the experimental probabilities.
Why: to see how close the empirical frequencies get to the theoretical 0.5 as trials increase.
Result from this run: heads = 5016, tails = 4984 → P(heads) ≈ 0.5016, P(tails) ≈ 0.4984.

(b) Two dice (probability of sum = 7)
What I did: simulated 100,000 trials of rolling two fair six-sided dice, counted how often the sum equals 7, then computed the proportion.
Why: sum = 7 is the most likely sum; simulation checks the empirical probability ≈ theoretical 6/36 = 1/6 ≈ 0.1667.
Result from this run: count sum=7 = 16551 / 100000 → P(sum=7) ≈ 0.16551.

2 — At least one “6” in 10 rolls

What I did: wrote a function that repeats this experiment many times (100,000 trials), each trial rolling a die 10 times and checking if at least one roll is a six. The function returns the fraction of trials where at least one six occurred.
Why: this estimates the probability 
1
−
(
5
/
6
)
10
1−(5/6)
10
 by simulation.
Result from this run: P(at least one 6 in 10 rolls) ≈ 0.84033. (The exact value 
1
−
(
5
/
6
)
10
1−(5/6)
10
 ≈ 0.8385.)

3 — Conditional Probability & Bayes’ theorem

Problem: bag with 5 red, 7 green, 8 blue (20 total). Draw with replacement repeatedly and estimate 
𝑃
(
current is red
∣
previous was blue
)
P(current is red∣previous was blue).
What I did: simulated a length-1000 sequence of draws with replacement, recorded cases where the previous draw was blue and checked the color of current draw; computed the ratio. I also showed the Bayes reasoning: with replacement the draws are independent, so the conditional probability equals the marginal probability of red.
Why: independence (because of replacement) means 
𝑃
(
𝑐
𝑢
𝑟
𝑟
𝑒
𝑛
𝑡
=
𝑟
𝑒
𝑑
∣
𝑝
𝑟
𝑒
𝑣
𝑖
𝑜
𝑢
𝑠
=
𝑏
𝑙
𝑢
𝑒
)
=
𝑃
(
𝑟
𝑒
𝑑
)
P(current=red∣previous=blue)=P(red). Bayes' formula reduces to that.
Result from this run: simulated conditional ≈ 0.2660 vs theoretical P(red)=5/20 = 0.25 (difference due to simulation noise; increase trials to reduce noise).

4 — Discrete random variable (sample of size 1000)

Distribution: P(X=1)=0.25, P(X=2)=0.35, P(X=3)=0.40.
What I did: used numpy.random.choice with the given probabilities to generate 1000 independent samples, then computed empirical mean, variance, and standard deviation (I report both population variance and sample variance with ddof=1).
Why: to check empirical moments vs theoretical ones.
Result from this run:

empirical mean ≈ 2.118

variance (population, ddof=0) ≈ 0.64208

variance (sample, ddof=1) ≈ 0.64272

std ≈ 0.80130.

5 — Continuous random variable (Exponential)

What I did: simulated 2000 samples from an exponential distribution with mean = 5 (numpy.random.exponential(scale=5)), plotted a histogram (density) and overlaid the theoretical PDF 
𝑓
(
𝑥
)
=
1
5
𝑒
−
𝑥
/
5
f(x)=
5
1
	​

e
−x/5
.
Why: to visually confirm the sample matches the theoretical density.
What to look for: histogram shape should follow the decreasing exponential curve; I plotted the theoretical curve on the same axes.

6 — Central Limit Theorem (CLT) demonstration

What I did:

Generated a "population" of 10,000 uniform(0,1) random numbers.

Repeated 1000 times: sample (with replacement) n = 30 values from that population and compute the sample mean.

Plotted the uniform population histogram and the histogram of the 1000 sample means (two separate plots).
Why: the histogram of sample means should be approximately normal (bell shaped) even though the underlying distribution is uniform; CLT shows that sample means approach a normal distribution as sample size grows.
Result from this run: sample means have mean ≈ 0.4931 and variance ≈ 0.002647.
