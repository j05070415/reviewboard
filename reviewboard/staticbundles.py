from __future__ import unicode_literals

from djblets.staticbundles import (
    PIPELINE_JAVASCRIPT as DJBLETS_PIPELINE_JAVASCRIPT,
    PIPELINE_STYLESHEETS as DJBLETS_PIPELINE_STYLESHEETS)


# Media compression
PIPELINE_JAVASCRIPT = dict({
    '3rdparty': {
        'source_filenames': (
            'lib/js/babel-polyfill-6.5.0.js',
            'lib/js/flot/jquery.flot.min.js',
            'lib/js/flot/jquery.flot.pie.min.js',
            'lib/js/flot/jquery.flot.selection.min.js',
            'lib/js/flot/jquery.flot.time.min.js',
            'lib/js/underscore-1.8.3.min.js',
            'lib/js/backbone-1.0.0.min.js',
            'lib/js/jquery.cookie-1.4.1.js',
            'lib/js/jquery.form.js',
            'lib/js/jquery.timesince.js',
            'lib/js/moment-2.12.0.js',
            'lib/js/moment-timezone-0.5.2.js',
            'lib/js/selectize-0.12.1.js',
            'lib/js/ui.autocomplete.js',
            'lib/js/codemirror-5.26.min.js',
        ),
        'output_filename': 'lib/js/3rdparty.min.js',
    },
    '3rdparty-jsonlint': {
        'source_filenames': (
            'lib/js/jsonlint.js',
        ),
        'output_filename': 'lib/js/3rdparty-jsonlint.min.js',
    },
    'js-test-libs': {
        'source_filenames': (
            'lib/js/jasmine-2.4.1.js',
            'lib/js/jasmine-html-2.4.1.js',
            'lib/js/jasmine-boot-2.4.1.js',
            'lib/js/jasmine.suites-1.0.js',
            'lib/js/jasmine.hide-filtered-1.0.js',
            'lib/js/jasmine.sourcemaps-1.0.js',
            'lib/js/sourcemapped-stacktrace.js',
        ),
        'output_filename': 'rb/js/js-test-libs.min.js',
    },
    'js-tests': {
        'source_filenames': (
            'rb/js/collections/tests/filteredCollectionTests.js',
            'rb/js/configForms/models/tests/resourceListItemModelTests.js',
            'rb/js/diffviewer/collections/tests/diffReviewableCollectionTests.es6.js',
            'rb/js/diffviewer/models/tests/diffFileModelTests.js',
            'rb/js/diffviewer/models/tests/diffReviewableModelTests.js',
            'rb/js/diffviewer/models/tests/diffRevisionModelTests.js',
            'rb/js/diffviewer/models/tests/paginationModelTests.js',
            'rb/js/diffviewer/views/tests/diffReviewableViewTests.js',
            'rb/js/models/tests/commentEditorModelTests.js',
            'rb/js/models/tests/extraDataTests.js',
            'rb/js/models/tests/reviewRequestEditorModelTests.js',
            'rb/js/models/tests/uploadDiffModelTests.js',
            'rb/js/models/tests/userSessionModelTests.js',
            'rb/js/newReviewRequest/views/tests/branchesViewTests.js',
            'rb/js/newReviewRequest/views/tests/postCommitViewTests.js',
            'rb/js/newReviewRequest/views/tests/repositorySelectionViewTests.js',
            'rb/js/pages/models/tests/diffViewerPageModelTests.es6.js',
            'rb/js/pages/models/tests/pageManagerModelTests.js',
            'rb/js/pages/models/tests/reviewablePageModelTests.es6.js',
            'rb/js/pages/views/tests/diffViewerPageViewTests.es6.js',
            'rb/js/pages/views/tests/reviewablePageViewTests.es6.js',
            'rb/js/resources/collections/tests/repositoryBranchesCollectionTests.js',
            'rb/js/resources/collections/tests/repositoryCommitsCollectionTests.js',
            'rb/js/resources/collections/tests/resourceCollectionTests.js',
            'rb/js/resources/models/tests/baseCommentModelTests.js',
            'rb/js/resources/models/tests/baseCommentReplyModelTests.js',
            'rb/js/resources/models/tests/baseResourceModelTests.js',
            'rb/js/resources/models/tests/defaultReviewerModelTests.js',
            'rb/js/resources/models/tests/diffCommentModelTests.js',
            'rb/js/resources/models/tests/draftReviewModelTests.js',
            'rb/js/resources/models/tests/draftReviewRequestModelTests.js',
            'rb/js/resources/models/tests/fileAttachmentModelTests.js',
            'rb/js/resources/models/tests/fileAttachmentCommentModelTests.js',
            'rb/js/resources/models/tests/fileDiffModelTests.js',
            'rb/js/resources/models/tests/generalCommentModelTests.js',
            'rb/js/resources/models/tests/screenshotModelTests.js',
            'rb/js/resources/models/tests/screenshotCommentModelTests.js',
            'rb/js/resources/models/tests/repositoryBranchModelTests.js',
            'rb/js/resources/models/tests/repositoryCommitModelTests.js',
            'rb/js/resources/models/tests/reviewGroupModelTests.js',
            'rb/js/resources/models/tests/reviewModelTests.js',
            'rb/js/resources/models/tests/reviewReplyModelTests.js',
            'rb/js/resources/models/tests/reviewRequestModelTests.js',
            'rb/js/resources/models/tests/userFileAttachmentModelTests.js',
            'rb/js/resources/models/tests/validateDiffModelTests.js',
            'rb/js/reviewRequestPage/models/tests/changeEntryModelTests.es6.js',
            'rb/js/reviewRequestPage/models/tests/entryModelTests.es6.js',
            'rb/js/reviewRequestPage/models/tests/reviewEntryModelTests.es6.js',
            'rb/js/reviewRequestPage/models/tests/reviewReplyEditorModelTests.js',
            'rb/js/reviewRequestPage/models/tests/reviewRequestPageModelTests.es6.js',
            'rb/js/reviewRequestPage/models/tests/statusUpdatesEntryModelTests.es6.js',
            'rb/js/reviewRequestPage/views/tests/baseStatusUpdatesEntryViewTests.es6.js',
            'rb/js/reviewRequestPage/views/tests/issueSummaryTableViewTests.es6.js',
            'rb/js/reviewRequestPage/views/tests/reviewEntryViewTests.js',
            'rb/js/reviewRequestPage/views/tests/reviewReplyDraftBannerViewTests.js',
            'rb/js/reviewRequestPage/views/tests/reviewReplyEditorViewTests.js',
            'rb/js/reviewRequestPage/views/tests/reviewRequestPageViewTests.es6.js',
            'rb/js/reviewRequestPage/views/tests/reviewViewTests.es6.js',
            'rb/js/ui/views/tests/dialogViewTests.js',
            'rb/js/ui/views/tests/infoboxManagerViewTests.es6.js',
            'rb/js/ui/views/tests/notificationManagerTests.es6.js',
            'rb/js/ui/views/tests/scrollManagerViewTests.es6.js',
            'rb/js/ui/views/tests/textEditorViewTests.js',
            'rb/js/utils/tests/keyBindingUtilsTests.js',
            'rb/js/utils/tests/linkifyUtilsTests.es6.js',
            'rb/js/utils/tests/urlUtilsTests.js',
            'rb/js/views/tests/collectionViewTests.js',
            'rb/js/views/tests/commentDialogViewTests.js',
            'rb/js/views/tests/commentIssueBarViewTests.js',
            'rb/js/views/tests/diffFragmentQueueViewTests.es6.js',
            'rb/js/views/tests/diffFragmentViewTests.es6.js',
            'rb/js/views/tests/draftReviewBannerViewTests.js',
            'rb/js/views/tests/fileAttachmentThumbnailViewTests.js',
            'rb/js/views/tests/reviewDialogViewTests.js',
            'rb/js/views/tests/reviewRequestEditorViewTests.js',
            'rb/js/views/tests/screenshotThumbnailViewTests.js',
        ),
        'output_filename': 'rb/js/js-tests.min.js',
    },
    'common': {
        'source_filenames': (
            'rb/js/utils/consoleUtils.es6.js',
            'rb/js/utils/underscoreUtils.es6.js',
            'rb/js/common.es6.js',
            'rb/js/utils/apiErrors.js',
            'rb/js/utils/apiUtils.es6.js',
            'rb/js/utils/linkifyUtils.es6.js',
            'rb/js/utils/mathUtils.es6.js',
            'rb/js/utils/keyBindingUtils.es6.js',
            'rb/js/utils/urlUtils.js',
            'rb/js/collections/baseCollection.es6.js',
            'rb/js/collections/filteredCollection.es6.js',
            'rb/js/extensions/models/aliases.js',
            'rb/js/extensions/models/commentDialogHookModel.js',
            'rb/js/extensions/models/reviewDialogCommentHookModel.js',
            'rb/js/extensions/models/reviewDialogHookModel.js',
            'rb/js/extensions/models/reviewRequestActionHookModel.js',
            'rb/js/pages/models/pageManagerModel.js',
            'rb/js/pages/models/pageModel.es6.js',
            'rb/js/pages/views/basePageView.es6.js',
            'rb/js/models/extraDataModel.js',
            'rb/js/models/extraDataMixin.js',
            'rb/js/resources/utils/serializers.es6.js',
            'rb/js/resources/models/baseResourceModel.es6.js',
            'rb/js/resources/models/apiTokenModel.es6.js',
            'rb/js/resources/models/repositoryBranchModel.es6.js',
            'rb/js/resources/models/repositoryCommitModel.es6.js',
            'rb/js/resources/models/draftResourceChildModelMixin.es6.js',
            'rb/js/resources/models/draftResourceModelMixin.es6.js',
            'rb/js/resources/models/draftReviewRequestModel.es6.js',
            'rb/js/resources/models/reviewModel.es6.js',
            'rb/js/resources/models/draftReviewModel.es6.js',
            'rb/js/resources/models/baseCommentModel.es6.js',
            'rb/js/resources/models/baseCommentReplyModel.es6.js',
            'rb/js/resources/models/defaultReviewerModel.es6.js',
            'rb/js/resources/models/diffCommentModel.es6.js',
            'rb/js/resources/models/diffCommentReplyModel.es6.js',
            'rb/js/resources/models/diffModel.es6.js',
            'rb/js/resources/models/fileAttachmentModel.es6.js',
            'rb/js/resources/models/fileAttachmentCommentModel.es6.js',
            'rb/js/resources/models/fileAttachmentCommentReplyModel.es6.js',
            'rb/js/resources/models/generalCommentModel.es6.js',
            'rb/js/resources/models/generalCommentReplyModel.es6.js',
            'rb/js/resources/models/fileDiffModel.es6.js',
            'rb/js/resources/models/draftFileAttachmentModel.es6.js',
            'rb/js/resources/models/repositoryModel.es6.js',
            'rb/js/resources/models/reviewGroupModel.es6.js',
            'rb/js/resources/models/reviewReplyModel.es6.js',
            'rb/js/resources/models/reviewRequestModel.es6.js',
            'rb/js/resources/models/screenshotModel.es6.js',
            'rb/js/resources/models/screenshotCommentModel.es6.js',
            'rb/js/resources/models/screenshotCommentReplyModel.es6.js',
            'rb/js/resources/models/userFileAttachmentModel.es6.js',
            'rb/js/resources/models/validateDiffModel.es6.js',
            'rb/js/resources/collections/resourceCollection.es6.js',
            'rb/js/resources/collections/repositoryBranchesCollection.es6.js',
            'rb/js/resources/collections/repositoryCommitsCollection.es6.js',
            'rb/js/ui/views/centeredElementManager.es6.js',
            'rb/js/ui/views/dialogView.es6.js',
            'rb/js/ui/views/baseInfoboxView.es6.js',
            'rb/js/ui/views/infoboxManagerView.es6.js',
            'rb/js/ui/views/bugInfoboxView.es6.js',
            'rb/js/ui/views/inlineEditorView.es6.js',
            'rb/js/ui/views/notificationManager.es6.js',
            'rb/js/ui/views/reviewRequestInfoboxView.es6.js',
            'rb/js/ui/views/scrollManagerView.es6.js',
            'rb/js/ui/views/splitButtonView.es6.js',
            'rb/js/ui/views/textEditorView.es6.js',
            'rb/js/ui/views/userInfoboxView.es6.js',
            'rb/js/models/starManagerModel.js',
            'rb/js/models/userSessionModel.js',
            'rb/js/views/headerView.js',
            'rb/js/views/collectionView.es6.js',
            'rb/js/views/starManagerView.js',
        ),
        'output_filename': 'rb/js/base.min.js',
    },
    'account-page': {
        'source_filenames': (
            'rb/js/accountPrefsPage/views/apiTokensView.es6.js',
            'rb/js/accountPrefsPage/views/joinedGroupsView.es6.js',
            'rb/js/accountPrefsPage/views/oauthApplicationsView.es6.js',
            'rb/js/accountPrefsPage/views/oauthTokensView.es6.js',
        ),
        'output_filename': 'rb/js/account-page.min.js',
    },
    'config-forms': {
        'source_filenames': (
            'rb/js/configForms/base.js',
            'rb/js/configForms/models/resourceListItemModel.es6.js',
        ),
        'output_filename': 'rb/js/config-forms.min.js',
    },
    'datagrid-pages': {
        'source_filenames': (
            'rb/js/pages/models/datagridPageModel.js',
            'rb/js/pages/models/dashboardModel.js',
            'rb/js/pages/views/datagridPageView.js',
            'rb/js/pages/views/dashboardView.js',
        ),
        'output_filename': 'rb/js/dashboard.min.js',
    },
    'reviews': {
        'source_filenames': (
            # Note: These are roughly in dependency order.
            'rb/js/models/abstractCommentBlockModel.es6.js',
            'rb/js/models/abstractReviewableModel.es6.js',
            'rb/js/models/commentEditorModel.es6.js',
            'rb/js/models/commentIssueManagerModel.es6.js',
            'rb/js/models/fileAttachmentCommentBlockModel.es6.js',
            'rb/js/models/fileAttachmentReviewableModel.es6.js',
            'rb/js/models/regionCommentBlockModel.es6.js',
            'rb/js/models/reviewRequestEditorModel.es6.js',
            'rb/js/models/imageReviewableModel.es6.js',
            'rb/js/models/dummyReviewableModel.es6.js',
            'rb/js/models/screenshotCommentBlockModel.es6.js',
            'rb/js/models/screenshotReviewableModel.es6.js',
            'rb/js/models/textBasedCommentBlockModel.es6.js',
            'rb/js/models/textBasedReviewableModel.es6.js',
            'rb/js/models/uploadDiffModel.js',
            'rb/js/pages/models/reviewablePageModel.es6.js',
            'rb/js/pages/models/diffViewerPageModel.es6.js',
            'rb/js/pages/views/reviewablePageView.es6.js',
            'rb/js/pages/views/diffViewerPageView.es6.js',
            'rb/js/utils/textUtils.es6.js',
            'rb/js/views/abstractCommentBlockView.es6.js',
            'rb/js/views/abstractReviewableView.es6.js',
            'rb/js/views/commentDialogView.es6.js',
            'rb/js/views/commentIssueBarView.es6.js',
            'rb/js/views/diffFragmentQueueView.es6.js',
            'rb/js/views/diffFragmentView.es6.js',
            'rb/js/views/dndUploaderView.es6.js',
            'rb/js/views/draftReviewBannerView.es6.js',
            'rb/js/views/uploadAttachmentView.js',
            'rb/js/views/revisionSelectorView.js',
            'rb/js/views/fileAttachmentReviewableView.es6.js',
            'rb/js/views/fileAttachmentRevisionLabelView.es6.js',
            'rb/js/views/fileAttachmentRevisionSelectorView.js',
            'rb/js/views/fileAttachmentThumbnailView.js',
            'rb/js/views/floatingBannerView.js',
            'rb/js/views/regionCommentBlockView.es6.js',
            'rb/js/views/reviewDialogView.es6.js',
            'rb/js/views/reviewRequestFieldViews.es6.js',
            'rb/js/views/reviewRequestEditorView.es6.js',
            'rb/js/views/screenshotThumbnailView.js',
            'rb/js/views/imageReviewableView.es6.js',
            'rb/js/views/dummyReviewableView.es6.js',
            'rb/js/views/textBasedCommentBlockView.es6.js',
            'rb/js/views/textBasedReviewableView.es6.js',
            'rb/js/views/textCommentRowSelector.js',
            'rb/js/views/markdownReviewableView.es6.js',
            'rb/js/views/uploadDiffView.js',
            'rb/js/views/updateDiffView.js',
            'rb/js/diffviewer/models/diffCommentBlockModel.es6.js',
            'rb/js/diffviewer/models/diffCommentsHintModel.js',
            'rb/js/diffviewer/models/diffFileModel.js',
            'rb/js/diffviewer/models/diffReviewableModel.es6.js',
            'rb/js/diffviewer/models/diffRevisionModel.js',
            'rb/js/diffviewer/models/paginationModel.js',
            'rb/js/diffviewer/collections/diffFileCollection.js',
            'rb/js/diffviewer/collections/diffReviewableCollection.es6.js',
            'rb/js/diffviewer/views/chunkHighlighterView.js',
            'rb/js/diffviewer/views/diffCommentBlockView.es6.js',
            'rb/js/diffviewer/views/diffCommentsHintView.js',
            'rb/js/diffviewer/views/diffComplexityIconView.js',
            'rb/js/diffviewer/views/diffFileIndexView.js',
            'rb/js/diffviewer/views/diffReviewableView.es6.js',
            'rb/js/diffviewer/views/diffRevisionLabelView.js',
            'rb/js/diffviewer/views/diffRevisionSelectorView.js',
            'rb/js/diffviewer/views/paginationView.js',
        ),
        'output_filename': 'rb/js/reviews.min.js',
    },
    'review-request-page': {
        'source_filenames': (
            'rb/js/reviewRequestPage/base.js',
            'rb/js/reviewRequestPage/models/entryModel.es6.js',
            'rb/js/reviewRequestPage/models/reviewEntryModel.es6.js',
            'rb/js/reviewRequestPage/models/reviewReplyEditorModel.js',
            'rb/js/reviewRequestPage/models/reviewRequestPageModel.es6.js',
            'rb/js/reviewRequestPage/models/statusUpdatesEntryModel.es6.js',
            'rb/js/reviewRequestPage/models/changeEntryModel.es6.js',
            'rb/js/reviewRequestPage/views/entryView.es6.js',
            'rb/js/reviewRequestPage/views/baseStatusUpdatesEntryView.es6.js',
            'rb/js/reviewRequestPage/views/changeEntryView.es6.js',
            'rb/js/reviewRequestPage/views/initialStatusUpdatesEntryView.es6.js',
            'rb/js/reviewRequestPage/views/issueSummaryTableView.es6.js',
            'rb/js/reviewRequestPage/views/reviewEntryView.es6.js',
            'rb/js/reviewRequestPage/views/reviewReplyDraftBannerView.js',
            'rb/js/reviewRequestPage/views/reviewReplyEditorView.js',
            'rb/js/reviewRequestPage/views/reviewRequestPageView.es6.js',
            'rb/js/reviewRequestPage/views/reviewView.es6.js',
        ),
        'output_filename': 'rb/js/review-request-page.min.js',
    },
    'newReviewRequest': {
        'source_filenames': (
            # Note: These are roughly in dependency order.
            'rb/js/models/uploadDiffModel.js',
            'rb/js/newReviewRequest/models/postCommitModel.js',
            'rb/js/newReviewRequest/models/newReviewRequestModel.js',
            'rb/js/views/uploadDiffView.js',
            'rb/js/newReviewRequest/views/branchView.js',
            'rb/js/newReviewRequest/views/branchesView.js',
            'rb/js/newReviewRequest/views/commitView.js',
            'rb/js/newReviewRequest/views/commitsView.js',
            'rb/js/newReviewRequest/views/repositoryView.js',
            'rb/js/newReviewRequest/views/repositorySelectionView.js',
            'rb/js/newReviewRequest/views/postCommitView.js',
            'rb/js/newReviewRequest/views/preCommitView.js',
            'rb/js/newReviewRequest/views/newReviewRequestView.js',
        ),
        'output_filename': 'rb/js/newReviewRequest.min.js',
    },
    'oauth-edit': {
        'source_filenames': (
            'rb/js/accountPrefsPage/views/oauthClientSecretView.es6.js',
        ),
        'output_filename': 'rb/js/oauth.min.js',
    },
    'admin-dashboard': {
        'source_filenames': (
            'lib/js/jquery.masonry.js',
            'rb/js/admin/admin.js',
            'rb/js/admin/views/supportBannerView.js',
        ),
        'output_filename': 'rb/js/admin-dashboard.min.js',
    },
    'repositoryform': {
        'source_filenames': (
            'rb/js/admin/repositoryform.js',
        ),
        'output_filename': 'rb/js/repositoryform.min.js',
    },
    'webhooks-form': {
        'source_filenames': (
            'rb/js/admin/views/webhookFormView.js',
        ),
        'output_filename': 'rb/js/webhooks-form.min.js',
    },
    'widgets': {
        'source_filenames': (
            'rb/js/admin/views/relatedObjectSelectorView.es6.js',
            'rb/js/admin/views/relatedUserSelectorView.es6.js',
        ),
        'output_filename': 'rb/js/widgets.min.js',
    },
}, **DJBLETS_PIPELINE_JAVASCRIPT)


PIPELINE_STYLESHEETS = dict({
    'common': {
        'source_filenames': (
            'lib/css/codemirror.css',
            'lib/css/jquery-ui-1.8.24.min.css',
            'lib/css/font-awesome-4.3.0.min.css',
            'lib/css/selectize.default-0.12.1.css',
            'rb/css/assets/icons.less',
            'rb/css/layout/helpers.less',
            'rb/css/pages/base.less',
            'rb/css/pages/search.less',
            'rb/css/ui/banners.less',
            'rb/css/ui/boxes.less',
            'rb/css/ui/buttons.less',
            'rb/css/ui/datagrids.less',
            'rb/css/ui/forms.less',
            'rb/css/ui/infoboxes.less',
            'rb/css/ui/markdown.less',
            'rb/css/ui/menus.less',
            'rb/css/ui/sidebars.less',
            'rb/css/common.less',
        ),
        'output_filename': 'rb/css/common.min.css',
        'absolute_paths': False,
    },
    'js-tests': {
        'source_filenames': (
            'lib/css/jasmine-2.4.1.css',
            'rb/css/pages/js-tests.less',
        ),
        'output_filename': 'rb/css/js-tests.min.css',
        'absolute_paths': False,
    },
    'account-page': {
        'source_filenames': (
            'rb/css/pages/my-account.less',
        ),
        'output_filename': 'rb/css/account-page.min.css',
    },
    'reviews': {
        'source_filenames': (
            'rb/css/pages/diffviewer.less',
            'rb/css/pages/image-review-ui.less',
            'rb/css/pages/text-review-ui.less',
            'rb/css/pages/reviews.less',
            'rb/css/pages/review-request.less',
            'rb/css/ui/dnd-uploader.less',
            'rb/css/syntax.less',
        ),
        'output_filename': 'rb/css/reviews.min.css',
        'absolute_paths': False,
    },
    'newReviewRequest': {
        'source_filenames': (
            'rb/css/pages/newReviewRequest.less',
        ),
        'output_filename': 'rb/css/newReviewRequest.min.css',
        'absolute_paths': False,
    },
    'oauth': {
        'source_filenames': (
            'rb/css/pages/oauth.less',
        ),
        'output_filename': 'rb/css/oauth.min.css',
        'absolute_paths': False,
    },
    'admin': {
        'source_filenames': (
            'rb/css/pages/admin.less',
            'rb/css/pages/admin-dashboard.less',
            'rb/css/pages/admin-integrations.less',
        ),
        'output_filename': 'rb/css/admin.min.css',
        'absolute_paths': False,
    },
    'widgets': {
        'source_filenames': (
            'rb/css/ui/related-object-selector.less',
        ),
        'output_filename': 'rb/css/widgets.min.css',
        'absolute_paths': False,
    },
}, **DJBLETS_PIPELINE_STYLESHEETS)
