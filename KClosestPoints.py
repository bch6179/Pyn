package notTested;

[LinkedIn] Find K nearest (closest) neighbors from point (comparator/comparable, priority queue )
分类： 面试题目们
2015-03-31 15:37 91人阅读 评论(0) 收藏 举报
/**
This is for finding k nearest neighbor from the original point
using a MAX heap, each time if the dist is less than the MAX we put it into the q.
**/
public Collection<Point> getClosestPoints(Collection<Point> points, int k) {
    <Point> queue = new PriorityQueue<Point>(k);

    for (Point point : points) {
        if (queue.size() < k) {
            queue.offer(point);
        } else {
            if (queue.peek().compareTo(point) < 0) {
                queue.poll();
                queue.offer(point);
            }
        }
    }

    return queue;
}


class Point implements Comparable<Point> {
    int x, y;
    double dist;

    public Point(int x, int y, Point originPoint) {
        this.x = x;
        this.y = y;
        //Math.hypot() returns sqrt(x^2 + y^2)
        this.dist = Math.hypot(x - originPoint.x, y - originPoint.y);
    }

    //assuming the original point is (0,0)
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
        this.dist = Math.hypot(x , y );
    }

    @Override
    public int compareTo(Point that) {
        return Double.valueOf(that.dist).compareTo(dist);
    }

    @Override
    public String toString() {
        return "x: " + x + " y: " + y;
    }
}
public List<Point> findKClosest(Point[] p, int k) {  
    PriorityQueue<Point> pq = new PriorityQueue<>(10, new Comparator<Point>() {  
        @Override  
        public int compare(Point a, Point b) {  
            return (b.x * b.x + b.y * b.y) - (a.x * a.x + a.y * a.y);  
        }  
    });  
       
    for (int i = 0; i < p.length; i++) {  
        if (i < k)  
            pq.offer(p[i]);  
        else {  
            Point tmp = pq.peek();  
            if ((p[i].x * p[i].x + p[i].y * p[i].y) - (tmp.x * tmp.x + tmp.y * tmp.y) < 0) {  
                pq.poll();  
                pq.offer(p[i]);  
            }  
        }  
    }  
       
    List<Point> x = new ArrayList<>();  
    while (!pq.isEmpty())  
        x.add(pq.poll());  
       
    return x;  


//cc

down vote
accepted
In Python (from www.comp.mq.edu.au/):

def count_different_values(k_v1s, k_v2s):
    """kv1s and kv2s should be dictionaries mapping keys to 
    values.  count_different_values() returns the number of keys in 
    k_v1s and k_v2s that don't have the same value"""
    ks = set(k_v1s.iterkeys()) | set(k_v2s.iterkeys())
    return sum(1 for k in ks if k_v1s.get(k) != k_v2s.get(k))


def sum_square_diffs(x0s, x1s):
    """x1s and x2s should be equal-lengthed sequences of numbers.
    sum_square_differences() returns the sum of the squared differences 
    of x1s and x2s."""
    sum((pow(x1-x2,2) for x1,x2 in zip(x1s,x2s)))

def incr(x_c, x, inc=1):
    """increments the value associated with key x in dictionary x_c
    by inc, or sets it to inc if key x is not in dictionary x_c."""
    x_c[x] = x_c.get(x, 0) + inc

def count_items(xs, x_c=None):
    """returns a dictionary x_c whose keys are the items in xs, and 
    whose values are the number of times each item occurs in xs."""
    if x_c == None:
        x_c = {}
    for x in xs:
        incr(x_c, x)
    return x_c

def second(xy):
    """returns the second element in a sequence"""
    return xy[1]

def most_frequent(xs):
    """returns the most frequent item in xs"""
    x_c = count_items(xs)
    return sorted(x_c.iteritems(), key=second, reverse=True)[0][0]


class kNN_classifier:
    """This is a k-nearest-neighbour classifer."""
    def __init__(self, train_data, k, distf):
        self.train_data = train_data
        self.k = min(k, len(train_data))
        self.distf = distf

    def classify(self, x):
        Ns = sorted(self.train_data, 
                    key=lambda xy: self.distf(xy[0], x))
        return most_frequent((y for x,y in Ns[:self.k]))

    def batch_classify(self, xs):
        return [self.classify(x) for x in xs]

def train(train_data, k=1, distf=count_different_values):
    """Returns a kNN_classifer that contains the data, the number of
    nearest neighbours k and the distance function"""
    return kNN_classifier(train_data, k, distf)
also another implementation of www.umanitoba.ca/

#!/usr/bin/env python
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.
"""
This module provides code for doing k-nearest-neighbors classification.

k Nearest Neighbors is a supervised learning algorithm that classifies
a new observation based the classes in its surrounding neighborhood.

Glossary:
distance   The distance between two points in the feature space.
weight     The importance given to each point for classification. 


Classes:
kNN           Holds information for a nearest neighbors classifier.


Functions:
train        Train a new kNN classifier.
calculate    Calculate the probabilities of each class, given an observation.
classify     Classify an observation into a class.

    Weighting Functions:
equal_weight    Every example is given a weight of 1.

"""

import numpy

class kNN:
    """Holds information necessary to do nearest neighbors classification.

    Members:
    classes  Set of the possible classes.
    xs       List of the neighbors.
    ys       List of the classes that the neighbors belong to.
    k        Number of neighbors to look at.

    """
    def __init__(self):
        """kNN()"""
        self.classes = set()
        self.xs = []
        self.ys = []
        self.k = None

def equal_weight(x, y):
    """equal_weight(x, y) -> 1"""
    # everything gets 1 vote
    return 1

def train(xs, ys, k, typecode=None):
    """train(xs, ys, k) -> kNN

    Train a k nearest neighbors classifier on a training set.  xs is a
    list of observations and ys is a list of the class assignments.
    Thus, xs and ys should contain the same number of elements.  k is
    the number of neighbors that should be examined when doing the
    classification.

    """
    knn = kNN()
    knn.classes = set(ys)
    knn.xs = numpy.asarray(xs, typecode)
    knn.ys = ys
    knn.k = k
    return knn

def calculate(knn, x, weight_fn=equal_weight, distance_fn=None):
    """calculate(knn, x[, weight_fn][, distance_fn]) -> weight dict

    Calculate the probability for each class.  knn is a kNN object.  x
    is the observed data.  weight_fn is an optional function that
    takes x and a training example, and returns a weight.  distance_fn
    is an optional function that takes two points and returns the
    distance between them.  If distance_fn is None (the default), the
    Euclidean distance is used.  Returns a dictionary of the class to
    the weight given to the class.

    """
    x = numpy.asarray(x)

    order = []  # list of (distance, index)
    if distance_fn:
        for i in range(len(knn.xs)):
            dist = distance_fn(x, knn.xs[i])
            order.append((dist, i))
    else:
        # Default: Use a fast implementation of the Euclidean distance
        temp = numpy.zeros(len(x))
        # Predefining temp allows reuse of this array, making this
        # function about twice as fast.
        for i in range(len(knn.xs)):
            temp[:] = x - knn.xs[i]
            dist = numpy.sqrt(numpy.dot(temp,temp))
            order.append((dist, i))
    order.sort()

    # first 'k' are the ones I want.
    weights = {}  # class -> number of votes
    for k in knn.classes:
        weights[k] = 0.0
    for dist, i in order[:knn.k]:
        klass = knn.ys[i]
        weights[klass] = weights[klass] + weight_fn(x, knn.xs[i])

    return weights

def classify(knn, x, weight_fn=equal_weight, distance_fn=None):
    """classify(knn, x[, weight_fn][, distance_fn]) -> class

    Classify an observation into a class.  If not specified, weight_fn will
    give all neighbors equal weight.  distance_fn is an optional function
    that takes two points and returns the distance between them.  If
    distance_fn is None (the default), the Euclidean distance is used.
    """
    weights = calculate(
        knn, x, weight_fn=weight_fn, distance_fn=distance_fn)

    most_class = None
    most_weight = None
    for klass, weight in weights.items():
        if most_class is None or weight > most_weight:
            most_class = klass
            most_weight = weight
    return most_class

    http://126kr.com/article/7w0a412nkhd
    K-nearest neighbor algorithm implementation in Python from scratch