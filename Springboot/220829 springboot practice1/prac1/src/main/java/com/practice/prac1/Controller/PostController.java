package com.practice.prac1.Controller;

import com.practice.prac1.Domain.DTO.PostReqDTO;
import com.practice.prac1.Domain.DTO.PostResDTO;
import com.practice.prac1.Service.PostService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/post")
@RequiredArgsConstructor
public class PostController {

    private final PostService postService;

    @PostMapping("/register/{stageId}")
    public PostResDTO savePost(@PathVariable("stageId") Long stageId, @RequestBody PostReqDTO postReqDTO){
        return postService.savePost(stageId, postReqDTO);
    }

    @GetMapping("/{index}")
    public PostResDTO readPost(@PathVariable("index") Long index){
        return postService.readPost(index);
    }

    @PutMapping("/{index}")
    public PostResDTO updatePost(@PathVariable("index") Long index, @RequestBody PostReqDTO postReqDTO){
        return postService.updatePost(index,postReqDTO);
    }

    @DeleteMapping("/{index}")
    public Long deletePost(@PathVariable("index") Long index){
        return postService.deletePost(index);
    }

}
