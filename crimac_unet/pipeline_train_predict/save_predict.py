""""
Copyright 2021 the Norwegian Computing Center

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
"""

import time
import numpy as np
from pipeline_train_predict.pipeline import Config_Options, SegPipeUNet
from paths import *

if __name__ == '__main__':

    # Configuration options
    configuration = pipeline_config()
    opt = Config_Options(configuration)

    segpipe = SegPipeUNet(opt)
    # Save segmentation predictions
    print("Save predictions")
    start = time.time()
    segpipe.save_segmentation_predictions_in_zarr(selected_surveys=opt.selected_surveys,
                                                  resume=opt.resume_writing)
    print(f"Executed time for saving all prediction (h): {np.round((time.time() - start) / 3600, 2)}")