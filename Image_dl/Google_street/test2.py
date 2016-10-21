import PanoProcess as pp

name = "mVJp7_CdBsX80bkQSGX_1g"
pp.GetPanoByID(name,"image")
input_name = "image/pano_"+name+".jpg"
pp.CutPano(input_name,"image/cut")
