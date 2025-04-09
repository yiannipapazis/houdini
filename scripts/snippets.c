////////////////////////////////////////
// Point Wrangle
// X Z Gradient Box

vector2 pos = set(v@P.x,v@P.z)-chu('box_offset');
pos = (((abs(pos)-chu('box_size'))-1)/chf('box_falloff'))+1;
pos = clamp(pos,0,1);
float box = min(1-pos);

////////////////////////////////////////
//
//