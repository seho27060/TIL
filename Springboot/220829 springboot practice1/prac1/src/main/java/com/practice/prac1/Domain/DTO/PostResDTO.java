package com.practice.prac1.Domain.DTO;

import com.practice.prac1.Domain.Post;
import com.practice.prac1.Domain.Stage;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@Builder
public class PostResDTO {
    private Long id;

    private String title;

    private String content;

    private StageResDTO stage;
}
