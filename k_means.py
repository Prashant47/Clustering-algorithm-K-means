from utils import * 


def computeSSE(data, centers, clusterID):
    sse = 0 
    nData = len(data) 
    for i in range(nData):
        c = clusterID[i]
        sse += squaredDistance(data[i], centers[c]) 
        
    return sse 

def updateClusterID(data, centers):
    nData = len(data) 
    
    clusterID = [0] * nData
    # assign the closet center to each data point
    
    for i in range(nData):
	if squaredDistance(data[i],centers[0]) < squaredDistance(data[i],centers[1]) :
  		clusterID[i] = 0;
	else :
		clusterID[i] = 1;
    
    return clusterID

# K: number of clusters 
def updateCenters(data, clusterID, K):
    nDim = len(data[0])
    nData = len(data)
    centers = [[0] * nDim for i in range(K)]

    center1 = [0] * 2
    center2 = [0] * 2
    count1 = 0
    count2 = 0

    # recompute the centers based on current clustering assignment
    # If a cluster doesn't have any data points, in this homework, leave it to ALL 0s

    for i in range(nData):
    	if clusterID[i] == 0:
		center1 = [ sum(x) for x in zip(center1, data[i]) ]
		count1 = count1 + 1
	else :
		center2 = [ sum(x) for x in zip(center2, data[i]) ]
		count2 = count2 + 1

    center1 = [ x / count1 for x in center1 ]
    center2 = [ x / count2 for x in center2 ]

    centers[0] = center1
    centers[1] = center2
 
    return centers 

def kmeans(data, centers, maxIter = 100, tol = 1e-6):
    nData = len(data) 
    
    if nData == 0:
        return [];

    K = len(centers) 
    
    clusterID = [0] * nData
    
    if K >= nData:
        for i in range(nData):
            clusterID[i] = i
        return clusterID

    nDim = len(data[0]) 
    
    lastDistance = 1e100
    
    for iter in range(maxIter):
        clusterID = updateClusterID(data, centers) 
        centers = updateCenters(data, clusterID, K)
        
        curDistance = computeSSE(data, centers, clusterID) 
        if lastDistance - curDistance < tol or (lastDistance - curDistance)/lastDistance < tol:
            print "# of iterations:", iter 
            print "SSE = ", curDistance
            return clusterID
        
        lastDistance = curDistance
        
    print "# of iterations:", iter 
    print "SSE = ", curDistance
    return clusterID

