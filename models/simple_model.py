class SimpleModel:

    def __init__(self, campaigns, payments):
        self.campaigns = campaigns
        self.payments = payments

    def get_list(self, date, user_id):
        df = self.campaigns
        # keep only active campaigns;
        # campaigns from favourite charities should be higher;
        # recently published campaigns should be higher;
        return self.campaigns.sort_values(['published_at']).head(10)
