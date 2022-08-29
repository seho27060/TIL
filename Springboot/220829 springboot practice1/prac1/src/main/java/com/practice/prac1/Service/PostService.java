package com.practice.prac1.Service;

import com.practice.prac1.Domain.DTO.PostReqDTO;
import com.practice.prac1.Domain.DTO.PostResDTO;

public interface PostService {

    PostResDTO savePost(Long stageId, PostReqDTO postReqDTO);

    PostResDTO readPost(Long index);

    PostResDTO updatePost(Long index, PostReqDTO postReqDTO);

    Long deletePost(Long index);
}
