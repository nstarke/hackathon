from django.conf.urls import patterns, url

from .views import SearchView, IndexView, RepoDetailView, RepoReviewView, RepoRepView


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='landing-page'),
    url(r'^search/$', SearchView.as_view(), name='search-view'),
    url(r'^repo/(?P<pk>\d+)/review/$', RepoReviewView.as_view(), name='repo-review-view'),
    url(r'^repo/rep/$', RepoRepView.as_view(), name='repo-rep-view'),
    # THIS MUST BE LAST
    url(r'^repo/(?P<slug>.+)/$', RepoDetailView.as_view(), name='repo-detail-view'),
)
