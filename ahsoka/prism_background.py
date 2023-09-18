# A dummy class for now to test the pipeline
# function created by GitHub copilot

from jwst import datamodels

class PrismBackgroundStep:

    def process(self, input):
        """Perform background subtraction on a NIRSpec prism exposure.

        Parameters
        ----------
        input: JWST data model

        Returns
        -------
        result: JWST data model
            The background-subtracted input
        """

        # Open the input data model
        with datamodels.open(input) as input_model:

            # Do the background subtraction
            input_model.data -= input_model.meta.background.level

            # Return the background-subtracted input
            return input_model