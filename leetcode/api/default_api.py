# coding: utf-8

"""
    Leetcode API

    Leetcode API implementation.  # noqa: E501

    OpenAPI spec version: 1.0.1-1
    Contact: pv.safronov@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from leetcode.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_problems_topic_get(self, topic, **kwargs):  # noqa: E501
        """api_problems_topic_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_problems_topic_get(topic, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str topic: (required)
        :return: Problems
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.api_problems_topic_get_with_http_info(
                topic, **kwargs
            )  # noqa: E501
        else:
            (data) = self.api_problems_topic_get_with_http_info(
                topic, **kwargs
            )  # noqa: E501
            return data

    def api_problems_topic_get_with_http_info(self, topic, **kwargs):  # noqa: E501
        """api_problems_topic_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_problems_topic_get_with_http_info(topic, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str topic: (required)
        :return: Problems
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["topic"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_problems_topic_get" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'topic' is set
        if "topic" not in params or params["topic"] is None:
            raise ValueError(
                "Missing the required parameter `topic` when calling `api_problems_topic_get`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "topic" in params:
            path_params["topic"] = params["topic"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = [
            "cookieCSRF",
            "cookieSession",
            "headerCSRF",
            "referer",
        ]  # noqa: E501

        return self.api_client.call_api(
            "/api/problems/{topic}/",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Problems",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def graphql_post(self, **kwargs):  # noqa: E501
        """graphql_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graphql_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GraphqlQuery body: GraphQL query
        :return: GraphqlResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.graphql_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.graphql_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def graphql_post_with_http_info(self, **kwargs):  # noqa: E501
        """graphql_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.graphql_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GraphqlQuery body: GraphQL query
        :return: GraphqlResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graphql_post" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = [
            "cookieCSRF",
            "cookieSession",
            "headerCSRF",
            "referer",
        ]  # noqa: E501

        return self.api_client.call_api(
            "/graphql",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GraphqlResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def problems_problem_interpret_solution_post(self, problem, **kwargs):  # noqa: E501
        """problems_problem_interpret_solution_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.problems_problem_interpret_solution_post(problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str problem: (required)
        :param TestSubmission body: Solution to test
        :return: Interpretation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.problems_problem_interpret_solution_post_with_http_info(
                problem, **kwargs
            )  # noqa: E501
        else:
            (data) = self.problems_problem_interpret_solution_post_with_http_info(
                problem, **kwargs
            )  # noqa: E501
            return data

    def problems_problem_interpret_solution_post_with_http_info(
        self, problem, **kwargs
    ):  # noqa: E501
        """problems_problem_interpret_solution_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.problems_problem_interpret_solution_post_with_http_info(problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str problem: (required)
        :param TestSubmission body: Solution to test
        :return: Interpretation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["problem", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method problems_problem_interpret_solution_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'problem' is set
        if "problem" not in params or params["problem"] is None:
            raise ValueError(
                "Missing the required parameter `problem` when calling `problems_problem_interpret_solution_post`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "problem" in params:
            path_params["problem"] = params["problem"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = [
            "cookieCSRF",
            "cookieSession",
            "headerCSRF",
            "referer",
        ]  # noqa: E501

        return self.api_client.call_api(
            "/problems/{problem}/interpret_solution/",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Interpretation",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def problems_problem_submit_post(self, problem, **kwargs):  # noqa: E501
        """problems_problem_submit_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.problems_problem_submit_post(problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str problem: (required)
        :param Submission body: Solution to test
        :return: SubmissionId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.problems_problem_submit_post_with_http_info(
                problem, **kwargs
            )  # noqa: E501
        else:
            (data) = self.problems_problem_submit_post_with_http_info(
                problem, **kwargs
            )  # noqa: E501
            return data

    def problems_problem_submit_post_with_http_info(
        self, problem, **kwargs
    ):  # noqa: E501
        """problems_problem_submit_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.problems_problem_submit_post_with_http_info(problem, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str problem: (required)
        :param Submission body: Solution to test
        :return: SubmissionId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["problem", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method problems_problem_submit_post" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'problem' is set
        if "problem" not in params or params["problem"] is None:
            raise ValueError(
                "Missing the required parameter `problem` when calling `problems_problem_submit_post`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "problem" in params:
            path_params["problem"] = params["problem"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = [
            "cookieCSRF",
            "cookieSession",
            "headerCSRF",
            "referer",
        ]  # noqa: E501

        return self.api_client.call_api(
            "/problems/{problem}/submit/",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SubmissionId",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def submissions_detail_id_check_get(self, id, **kwargs):  # noqa: E501
        """submissions_detail_id_check_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submissions_detail_id_check_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Id id: Either submission id (int) or interpretation id (string) (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.submissions_detail_id_check_get_with_http_info(
                id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.submissions_detail_id_check_get_with_http_info(
                id, **kwargs
            )  # noqa: E501
            return data

    def submissions_detail_id_check_get_with_http_info(
        self, id, **kwargs
    ):  # noqa: E501
        """submissions_detail_id_check_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submissions_detail_id_check_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Id id: Either submission id (int) or interpretation id (string) (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submissions_detail_id_check_get" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `submissions_detail_id_check_get`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = [
            "cookieCSRF",
            "cookieSession",
            "headerCSRF",
            "referer",
        ]  # noqa: E501

        return self.api_client.call_api(
            "/submissions/detail/{id}/check/",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse200",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
