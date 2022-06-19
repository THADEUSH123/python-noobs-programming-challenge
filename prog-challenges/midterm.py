
# {
#    "source": [
#     "## 7. Birthday planning (15 pts)\n",
#     "\n",
#     "Suppose you record a list of birthdays for your classmates, recorded as month day tuples.  An example is given below."
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 19,
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "# The 2nd to last tuple needs the int(2) in it so that it is uniquely stored in memory compared to (2,8)\n",
#     "# Under the hood Python 3.7 changed how these are stored so (2,8) and (2,8) are stored in the same location\n",
#     "# and then the algorithm below doesn't work\n",
#     "\n",
#     "dates = [(3,14),(2,8),(10,25),(5,17),(3,2),(7,25),(4,30),(8,7),(int(2),8),(1,22)]"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "You read about the famous birthday problem and you become interested in the number of pairs of classmates that share the same birthday.  Below is an algorithm you write to do this. (Note: the ```is``` operator tests that two operands point to the same object)"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 20,
#    "metadata": {},
#    "outputs": [
#     {
#      "name": "stdout",
#      "output_type": "stream",
#      "text": [
#       "Total birthday pairs: 1\n"
#      ]
#     }
#    ],
#    "source": [
#     "count = 0\n",
#     "\n",
#     "for person_a in dates:\n",
#     "    for person_b in dates:\n",
#     "        # Make sure we have different people        \n",
#     "        \n",
#     "        if person_a is person_b:\n",
#     "            continue\n",
#     "            \n",
#     "        # Check both month and day\n",
#     "        if person_a[0] == person_b[0] and person_a[1] == person_b[1]:\n",
#     "            count += 1\n",
#     "            \n",
#     "# We counted each pair twice (e.g. jane-bob and bob-jane) so divide by 2:\n",
#     "print(\"Total birthday pairs:\", count//2)"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "7.1. What is the (tightest) Big-O running time bound for the above algorithm?  You may assume that simple operations like equality check, addition, and print take constant time."
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {
#     "collapsed": true
#    },
#    "source": [
#     "**Your answer here**"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "7.2. You notice that your algorithm is inefficient in that it counts each pair twice.  For example, it will increment count once when person_a is Jane and person_b is Bob, and again when person_a is Bob and person_b is Jane.  Below, revise the algorithm so that it only looks at each pair once."
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": null,
#    "metadata": {
#     "collapsed": true
#    },
#    "outputs": [],
#    "source": [
#     "# Your code here"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "7.3. What is the (tightest) Big-O running time bound for your new algorithm?  What does this tell you about whether your revision was worth making?"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "**Your answer here**"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "7.4. Finally, create a third revision of your algorithm which has a faster Big-O running time bound that both the previous algorithms."
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 5,
#    "metadata": {
#     "collapsed": true
#    },
#    "outputs": [],
#    "source": [
#     "# Your code here"
#    ]
#   },
#   {
#    "cell_type": "markdown",
#    "metadata": {},
#    "source": [
#     "7.5. What is the (tightest) Big-O running time bound for your last algorithm?  Explain what trade-off you made to have a faster running time."
#    ]
#   },

dates = [(3,14),(2,8),(10,25),(5,17),(3,2),(7,25),(4,30),(8,7),(int(2),8),(1,22)]

count = 0
for person_a in dates:
    for person_b in dates:
        # Make sure we have different people
        if person_a is person_b:
            continue

        # Check both month and day\n",
        if person_a[0] == person_b[0] and person_a[1] == person_b[1]:
            count += 1
    # We counted each pair twice (e.g. jane-bob and bob-jane) so divide by 2:\n",
print("Total birthday pairs(7.1):" + str(int(count/2)))


# Answer for 7.1:  The algorythm is O(n^2).


# Answer for 7.2:
dates = [(3,14),(2,8),(10,25),(5,17),(3,2),(7,25),(4,30),(8,7),(int(2),8),(1,22)]
count = 0
for person_a in dates:
    dates2 = dates
    dates2.remove(person_a)
    for person_b in dates2:
        # Check both month and day\n",
        if person_a[0] == person_b[0] and person_a[1] == person_b[1]:
            count += 1

    # We counted each pair once.
print("Total birthday pairs(7.2):" + str(count))


# Answer for 7.3: It is still O(n^2). This change does not make the code more performent relative to the 7.1 solution if given a similar sized input. This is likely due to the constant time cost of creating a second list and removing an element, which requires more processing than simply dividing by two at the end. Furthermore, this solution is not a performance improvement from a Big-O perspective.


# Answer for 7.4 below
from collections import defaultdict
dates = [(3,14),(2,8),(10,25),(5,17),(3,2),(7,25),(4,30),(8,7),(int(2),8),(1,22)]
counts = defaultdict(int)
for person in dates:
    counts[person] += 1
print("Total birthday pairs(7.4):" + str(sum(counts.values()) - len(counts)))


# Answer for 7.5: The algorythm is O(n). I traded memory(used more) for compute(used less) to achieve this outcome.
