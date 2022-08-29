package com.practice.prac1.Service;

import com.practice.prac1.Domain.DTO.PostReqDTO;
import com.practice.prac1.Domain.DTO.PostResDTO;
import com.practice.prac1.Domain.DTO.StageResDTO;
import com.practice.prac1.Domain.Post;
import com.practice.prac1.Domain.Stage;
import com.practice.prac1.Repository.PostRepository;
import com.practice.prac1.Repository.StageRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@Transactional
public class PostServiceImpl implements PostService{
    private final PostRepository postRepository;
    private final StageRepository stageRepository;

    @Override
    public PostResDTO savePost(Long stageId, PostReqDTO postReqDTO) {
        Optional<Stage> stage = stageRepository.findById(stageId);
        if(stage.isPresent()){
            Stage innerStage = stage.get();
            Post post = Post.builder()
                    .stage(innerStage)
                    .title(postReqDTO.getTitle())
                    .content(postReqDTO.getContent())
                    .build();
            Post innerPost = postRepository.save(post);
            StageResDTO stageResDTO = StageResDTO.builder()
                    .id(innerStage.getId())
                    .level(innerStage.getLevel())
                    .title(innerStage.getTitle())
                    .content(innerStage.getContent())
                    .build();
            PostResDTO postResDTO = PostResDTO.builder()
                    .id(innerPost.getId())
                    .title(innerPost.getTitle())
                    .content(innerPost.getContent())
                    .stage(stageResDTO)
                    .build();
            return postResDTO;
        }
        return null;
    }

    @Override
    public PostResDTO readPost(Long index) {
        Optional<Post> post = postRepository.findById(index);
        if (post.isPresent()){
            Post innerPost = post.get();
            StageResDTO stageResDTO = StageResDTO.builder()
                    .id(innerPost.getStage().getId())
                    .level(innerPost.getStage().getLevel())
                    .title(innerPost.getStage().getTitle())
                    .content(innerPost.getStage().getContent())
                    .build();
            PostResDTO postResDTO = PostResDTO.builder()
                    .id(innerPost.getId())
                    .title(innerPost.getTitle())
                    .stage(stageResDTO)
                    .content(innerPost.getContent())
                    .build();
            return postResDTO;
        }
        return null;
    }

    @Override
    public PostResDTO updatePost(Long index, PostReqDTO postReqDTO) {
        Optional<Post> post = postRepository.findById(index);
        if (post.isPresent()){
            Post innerPost = post.get();
            innerPost.updatePost(postReqDTO);
            StageResDTO stageResDTO = StageResDTO.builder()
                    .id(innerPost.getStage().getId())
                    .level(innerPost.getStage().getLevel())
                    .title(innerPost.getStage().getTitle())
                    .content(innerPost.getStage().getContent())
                    .build();
            PostResDTO postResDTO = PostResDTO.builder()
                    .title(postReqDTO.getTitle())
                    .stage(stageResDTO)
                    .content(postReqDTO.getContent())
                    .id(innerPost.getId())
                    .build();
            return postResDTO;
        }
        return null;
    }

    @Override
    public Long deletePost(Long index) {
        Optional<Post> post = postRepository.findById(index);
        if (post.isPresent()){
            postRepository.deleteById(index);
            return index;
        }
        return null;
    }
}
