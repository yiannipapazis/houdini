bisect[0] = point(1, 'bisect', 0);
bisect[1] = point(1, 'bisect', 1);

vector pos[];
pos[0] = point(1,'P',0);
pos[1] = point(1,'P',1);

vector p = chv('pos');

float mag[];
// Intersect point with same vector
mag[0] = dot(pos[0]-p,bisect[0]); // Calculate how far we need to travel to get to point along vector
// Intersect point with different vector
mag[1] = dot(pos[1]-p,bisect[1]) / dot(bisect[0],bisect[1]);
// Calculate distance between two points along vector
// Divided by distance traveled along said vector

vector i[]; // Intersections
i[0] = p + (bisect[0]*mag[0]);
i[1] = p + (bisect[0]*mag[1]);

int pts[];
pts[0] = addpoint(0,i[0]);
pts[1] = addpoint(0,p);
pts[2] = addpoint(0,i[1]);
addprim(0,'polyline',pts);